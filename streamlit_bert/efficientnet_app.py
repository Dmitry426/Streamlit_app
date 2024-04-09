import time

import streamlit
from PIL import Image

from streamlit_bert.services.loader import get_base64_of_bin_file
from streamlit_bert.services.utils import query

streamlit.markdown('<h1 style="color:white;">Inference Google Efficientnet-b7</h1>', unsafe_allow_html=True)


def set_png_as_page_bg(png_file):
    """
    Set a PNG image file as the background of the Streamlit page.

    Args:
        png_file (str): Path to the PNG image file.

    Returns:
        None
    """
    bin_str = get_base64_of_bin_file(png_file)
    if bin_str:
        page_bg_img = '''
        <style>
        .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: scroll; # doesn't work
        }
        </style>
        ''' % bin_str

        streamlit.markdown(page_bg_img, unsafe_allow_html=True)
    return


def efficientnet_app():
    """
    Run an application for EfficientNet image classification with a custom background.

    Returns:
        None
    """
    set_png_as_page_bg(
        './static/backgrounds/geometry-geometric-web-dark-wallpaper-38267d8820d01cd810ac21ae7822848a.jpg')

    upload = streamlit.file_uploader(':red[Insert image for classification]', type=['png', 'jpg'])
    c1, c2 = streamlit.columns(2)
    if upload is not None:
        upload_copy = upload
        output = query(upload.read())
        if output:
            im = Image.open(upload_copy)
            c1.header('Input Image')
            c1.image(im)

            time.sleep(1)
            c2.header(':black[Output]')
            c2.subheader('Predicted class')
            c2.write(output)


if __name__ == '__main__':
    efficientnet_app()
