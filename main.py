from icrawler.builtin import GoogleImageCrawler


def google_img_downloader():
    filters = dict(
        type='photo',
        # color='blackandwhite',
        size='large',
        # licence='noncommercial, commercial',
        # date=((2020, 1, 1), (2022, 5, 14))
    )
    crawler = GoogleImageCrawler(storage={"root_dir": './img'}) # путь сохранения картинок
    # crawler.crawl(keyword='mr.robot', max_num=5) 
    # crawler.crawl(keyword='mercedes 216', max_num=5, min_size=(1000,1000), overwrite=True)
    crawler.crawl(
        keyword='Miami Forida', 
        max_num=5, 
        min_size=(1000,1000), 
        overwrite=True,
        filters=filters,
        file_idx_offset='auto'
        )


def main():
    google_img_downloader()


if __name__ == '__main__':
    main()