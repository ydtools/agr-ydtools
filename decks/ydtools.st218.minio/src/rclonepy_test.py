
def test_rclone_tree():
    import rclonepy
    from pathlib import Path
    
    me_parent_p = Path(__file__).parent
    name = Path(__file__).name

    the_tree = rclonepy.tree('..')
    
    assert len(the_tree.splitlines()) > 3
    assert name in the_tree
    print(the_tree)


def test_rclone_tree():
    import rclonepy
    from pathlib import Path
    
    me_parent_p = Path(__file__).parent
    name = Path(__file__).name

    the_data = rclonepy.get_data('minio:test-b/hw.text.txt')
    assert 'Hello' in the_data