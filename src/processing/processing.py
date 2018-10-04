import pathos.multiprocessing as mp
import ocr.ocr as ocr
from processing.processing_results import ProcessingResults

pool = mp.Pool(processes=mp.cpu_count())


def get_batch_text(objects, parallel):
    if parallel:
        return pool.map(lambda x: ProcessingResults(x.index, ocr.get_text(x.absolute_path_string), x.reason), objects)
    else:
        return map(lambda x: ProcessingResults(x.index, ocr.get_text(x.absolute_path_string), x.reason), objects)
