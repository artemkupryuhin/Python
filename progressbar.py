from progress.bar import Bar

print(__name__)
bar = Bar('Processing', max=200000)
for i in range(200000):
    # Do some work
    bar.next()
bar.finish()