import click
import gpxpy
import os
import gpxpy.gpx

@click.command()
@click.argument('directory', type=click.Path(exists=True, file_okay=False, dir_okay=True, resolve_path=True, readable=True))
@click.option('--unit', default='f', type=click.Choice(['f','m'], case_sensitive=False), show_default=True, help="Unit to output total vert in")
def vertcounter(directory, unit):
    """Analyze GPX files in a directory and output the total vertical distance traveled uphill."""

    dir_contents = os.listdir(directory)
    filenames = [f for f in dir_contents if os.path.isfile(directory+'/'+f) and f.endswith(".gpx")]
    paths = [directory+'/'+f for f in filenames]

    total_vert_meters = 0
    for filename in paths:
        with open(filename) as file:
            total_vert_meters += vert_for_gpx_file(file)

    if(unit == "f"):
        print("Total vert (feet): {:.2f}".format(total_vert_meters * 3.280839895))
    else:
        print("Total vert (meters): {:.2f}".format(total_vert_meters))

# Get uphill vert for file path in meters
def vert_for_gpx_file(gpxfile):
    try:
        gpx = gpxpy.parse(gpxfile)
    except:
        raise click.UsageError("Error: Failed to parse GPX file {}. Check that the file is not corrupted.".format(gpxfile), ctx=None)

    if(not len(gpx.tracks) == 1):
        raise click.UsageError("Error: GPX file must contain exactly one track. Found {} tracks in file {}".format(len(gpx.tracks), gpxfile), ctx=None)
    track = gpx.tracks[0]

    return track.get_uphill_downhill().uphill

if __name__ == "__main__":
    vertcounter()