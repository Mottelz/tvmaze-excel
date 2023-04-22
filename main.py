from tvmaze import search_for_show
from excel_writer import write_dict_to_file


def show_to_string(show):
    year = show.get("premiered")
    return f'{show.get("name")}\t({year[:4] if year else ""})'


def main():
    search_term = input("Enter your search term: ")
    shows = search_for_show(search_term)
    for i in range(len(shows)):
        show = show_to_string(shows[i])
        print(f"{i}:\t{show}")
    show_to_save = shows[eval(input("Enter the show to save: "))]
    write_dict_to_file('showlist', 'shows', show_to_save)


if __name__ == "__main__":
    main()
