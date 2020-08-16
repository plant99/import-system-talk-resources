from urlimport import github_repo

with github_repo('plant99', 'felicette'):
    from felicette.setup import dependencies
    print(dependencies)