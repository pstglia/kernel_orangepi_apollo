#!/usr/bin/env python3
import sys, io, tarfile

def main():
    # Lê os dados gzipados do stdin
    data = sys.stdin.buffer.read()
    # Abre o stream gzipado como tar
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
        # Extrai o conteúdo dos arquivos e escreve no stdout
        for member in tar.getmembers():
            f = tar.extractfile(member)
            if f:
                sys.stdout.buffer.write(f.read())

if __name__ == "__main__":
    main()

