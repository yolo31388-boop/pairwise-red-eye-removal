import pytest
import imaging.red_eye_removal as mod

CASES = [
    ("detect_full_res", (1,)),
    ("mask_chroma_cluster", (1,)),
    ("keep_highlight", (1,)),
    ("infer_per_image", (1,)),
    ("write_back_depth", (1,)),
    ("feather_edge", (1,)),
    ("load", (1,)),
    ("detect", (1,)),
    ("repair", (1,)),
    ("export", (1,)),
    ("validate_redeye", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
