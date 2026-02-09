import mmma
import os
import utils
import shutil

# Set global variables:
SRC_FOLDER = os.path.join(os.getcwd(), "data", "sources")
OUT_FOLDER = os.path.join(os.getcwd(), "travail", "dps", "output", "01-preprocess")
ACCEPTED_FILES = ["mp4", "wav"]

def preprocess_corpus(corpus : mmma.Corpus):
    
    # Create temporary directory:
    temp_dir = os.path.join(os.getcwd(), "dps_temp")
    if os.path.isdir(temp_dir) == False:
        os.makedirs(temp_dir)

    # Convert to audio:
    if corpus.media_type == "Video":
        corpus = corpus.render(os.path.join(temp_dir, "audio_temp.wav"), video = False, audio = True)

    
    
    # Remove temporary directory:
    shutil.rmtree(temp_dir)

def process():
    # Get the source files:
    src_files = utils.collect_files(SRC_FOLDER, ACCEPTED_FILES)

    # Create output destinations:
    if os.path.isdir(OUT_FOLDER) == False:
        os.makedirs(os.path.join(OUT_FOLDER, "corpora"))
        os.makedirs(os.path.join(OUT_FOLDER, "processed_media"))
        os.makedirs(os.path.join(OUT_FOLDER, "mapping"))

    # Convert the sources into mmma corpora:
    corpora = []
    for source in src_files:
        corpora.append(mmma.Corpus(render_path = source))

    # Preprocess the files:
    for corpus in corpora:
        preprocess_corpus(corpus)

process()