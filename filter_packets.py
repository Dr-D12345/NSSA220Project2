def filter(inputFile, outputFile):
	infile = open(inputFile, 'r')
	outfile = open(outputFile, "w+")
	fileline = infile.readline()
	outfile.write(fileline)
	while fileline:
		if "Echo" in fileline:

			outfile.write(fileline)
			while fileline.startswith("No.") == False:
				fileline = infile.readline()
				outfile.write(fileline)
		fileline = infile.readline()
	infile.close()
	outfile.close()
