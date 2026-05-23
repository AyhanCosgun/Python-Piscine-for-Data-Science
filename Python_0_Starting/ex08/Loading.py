import os


def ft_tqdm(lst: range):
    total = len(lst)
    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80

    right_padding = len(" [00:01<00:00, 191.61it/s]")

    for current, elem in enumerate(lst, 1):
        percent = int((current) / total * 100)
        prefix = f"{percent:3d}%|["
        suffix = f"]| {current}/{total}"

        bar_size = 4

        if terminal_width < len(prefix) + bar_size + len(suffix) \
                + right_padding:
            if terminal_width > len(prefix) + len(suffix) + bar_size:
                # right_padding cancelled
                bar_size = terminal_width - len(prefix) - len(suffix)
        else:
            bar_size = terminal_width - len(prefix) - len(suffix) \
                - right_padding

        filled = int(bar_size * (current) / total)
        if filled > 0:
            bar = '=' * (filled - 1) + '>' + ' ' * (bar_size - filled)
        else:
            bar = '>' + ' ' * (bar_size - 1)

        print(f'\r{prefix}{bar}{suffix}', end='', flush=True)
        yield elem
