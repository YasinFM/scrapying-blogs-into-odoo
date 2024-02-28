import get_blog_html_ids
import get_HTML
import external_api
import delete_folder_content



flag = get_blog_html_ids.get_ids_via_curl()

if flag:
    get_HTML.html_file()

    external_api.upload_html_files_as_blogs("html-files")

    delete_folder_content.delete_folder_contents("html-files")
