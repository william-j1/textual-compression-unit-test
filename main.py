import argparse
import zlib
import gzip
import bz2
import lzma
import lz4.frame
import snappy
import zstandard as zstd
import brotli

def main():

    # prototype string
    ps = ""
    try:
        parser = argparse.ArgumentParser(description="process textual input")
        parser.add_argument('t', type=str, help='the prototype string input')
        args = parser.parse_args()
        ps = args.t
    except:
        ps = "Untitled[]cube:RmlsdGVy:150#cylinder:SW50YWtl:100:1200#cylinder:UGFzc3RocnU=:100:2000#rectangular_tank:UmVzZXJ2b2ly:2000:300:300@1=1=1=1"

    # convert the input string to bytes, as compression functions require byte inputs
    snippet = ps.encode('utf-8')

    # compress the prototype string and store the resultant widths
    widths = {}
    widths['zlib'] = len(zlib.compress(snippet))
    widths['gzip'] = len(gzip.compress(snippet))
    widths['bz2'] = len(bz2.compress(snippet))
    widths['lzma'] = len(lzma.compress(snippet))
    widths['lz4'] = len(lz4.frame.compress(snippet))
    widths['snappy'] = len(snappy.compress(snippet))
    cctx = zstd.ZstdCompressor()
    widths['zstandard'] = len(cctx.compress(snippet))
    widths['brotli'] = len(brotli.compress(snippet))

    # sort by values to enlist the best at the top/front
    widths = dict(sorted(widths.items(), key=lambda item: item[1]))

    # print results
    print('\nSNIPPET\n' + ps + '\n\nSIZE OF ' + str(len(snippet)) +' BYTES\n')
    for method, size in widths.items():
        ei = round(1.0 - (size/len(snippet)), 4)
        print(f"{method.upper()}: {size} bytes with efficiency benefit of {ei}")

if __name__ == "__main__":
    main()
