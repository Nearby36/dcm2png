import gdcm
import sys

def dc(inputFile, outputFile):
	reader = gdcm.ImageReader()
	reader.SetFileName(inputFile)

	if not reader.Read():
		sys.exit(1)

	change = gdcm.ImageChangeTransferSyntax()
	change.SetTransferSyntax( gdcm.TransferSyntax(gdcm.TransferSyntax.ImplicitVRLittleEndian) )
	change.SetInput( reader.GetImage() )
	if not change.Change():
		sys.exit(1)

	writer = gdcm.ImageWriter()
	writer.SetFileName(outputFile)
	writer.SetFile( reader.GetFile() )
	writer.SetImage( change.GetOutput() )

	if not writer.Write():
		sys.exit(1)