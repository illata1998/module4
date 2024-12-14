# BEGIN
def merge(file1, file2, out):
    with (
        open(file1, 'r') as f1,
        open(file2, 'r') as f2,
        open(out, 'w') as fout,
    ):
        diff1 = []
        diff2 = []
        for line1, line2 in zip(f1, f2):
            if line1 == line2:
                if diff1 or diff2:
                    fout.write(make_diff_view(diff1, diff2))
                    diff1 = []
                    diff2 = []
                fout.write(line1)
            else:
                diff1.append(line1)
                diff2.append(line2)
        if diff1 or diff2:
            fout.write(make_diff_view(diff1, diff2))


def make_diff_view(diff1, diff2):
    template = f">>>file1>>>\n{''.join(diff1)}=====\n{''.join(diff2)}<<<file2<<<\n"  # noqa: E501
    return template
# END
