import os
import shutil
import tempfile
# 3rd party
import click


class DuplicateLinesCleaner(object):

    def __init__(self, infile, outfile, preserve_order=True,
                 top_to_bottom=True):
        self.preserve_order = preserve_order
        self.top_to_bottom = top_to_bottom
        self.infile = infile
        self.outfile = outfile
        self.tempfile = ''

    def remove_duplicates(self):
        dset = set()
        write_to_same_file = False

        self.tempfile = tempfile.NamedTemporaryFile(mode="w", delete=False)

        if self.infile == self.outfile:
            write_to_same_file = True

        with open(self.tempfile.name, 'w') as out:
            for line in open(self.infile):
                if line not in dset:
                    out.write(line)
                    dset.add(line)

        dst = self.outfile
        if write_to_same_file:
            # cp tempfile to infile
            dst = self.infile
        shutil.copy(self.tempfile.name, dst)
        # delete tempfile
        os.remove(self.tempfile.name)


@click.command()
@click.option('--infile', '-i', required=True,
              help='the inputfile you want to delete the duplicate lines from')
@click.option('--outfile', '-o', required=True,
              help='the outputfile you want to write to')
def main(infile, outfile):
    """duplines cli eliminates duplicate lines in a file and keeps the sorting order"""

    try:
        dlc = DuplicateLinesCleaner(infile, outfile)
        dlc.remove_duplicates()
        click.echo('cleaned up duplicates')
    except FileNotFoundError as fnf:
        click.echo(message=fnf, err=True)
    except Exception as e:
        click.echo(message=e, err=True)
