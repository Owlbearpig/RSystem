from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


def main():
    # filename = "capture1_h.txt"
    filename = "capture_ascii.txt"

    file_path = Path("captures") / filename

    eof = "0x21 0x45 0x30 0x30 0x30 0x32"  # frame split
    word_len = 8  # data slice length
    with open(file_path, "rb") as file:
        dump = file.read()
        h_ = " ".join([hex(c) for c in dump])

        frames = h_.split(eof)
        print(f"number of frames: {len(frames)}")
        vals = []
        for frame_idx, frame in enumerate(frames):
            # print(frame, len(frame), "\n")

            hex_data = frame.replace(" 0x", "")
            hex_data = hex_data.replace(" ", "")

            pad = int(word_len-np.mod(len(hex_data), word_len))
            hex_data = hex_data.ljust(len(hex_data) + pad, "0")

            for i in range(len(hex_data) // word_len):
                data_slice = hex_data[word_len*i:word_len*(i + 1)]
                val = int(data_slice, 16)
                vals.append(val)

            # print(hex_data, len(hex_data), "\n")
            plt.plot(vals, label=f"frame idx: {frame_idx}")

            vals = []

    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
