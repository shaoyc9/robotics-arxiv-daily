import arxiv

result = arxiv.Search(
    query = "",
    max_results = 100,
    sort_by = arxiv.SortCriterion.SubmittedDate
)
for result in result.results():
    print(result.entry_id, '->', result.title)