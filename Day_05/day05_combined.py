from collections import deque, defaultdict

def main():
    sum_rules('page_rules.txt')

def read_input(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip() != '']
    return lines


def parse_rules_and_updates(lines):
    rules = []
    updates = []
    # separete rules and updates based on '|' or ','
    for line in lines:
        if '|' in line:
            rules.append(line)
        elif ',' in line:
            updates.append(line)
    return rules, updates


def check_update_order(update_line, rules):
    pages = [int(x.strip()) for x in update_line.split(',')]
    page_index = {p: i for i, p in enumerate(pages)}

    for rule_line in rules:
        left_str, right_str = rule_line.split('|')
        left, right = int(left_str), int(right_str)

        # only check rules if both pages are in the update
        if left in page_index and right in page_index:
            if page_index[left] > page_index[right]:
                return False
    return True


def topological_sort(pages, rules):
    # Build graph for the given subset of pages
    graph = defaultdict(list)
    indegree = {p: 0 for p in pages}

    # Add edges according to the applicable rules
    for rule_line in rules:
        left_str, right_str = rule_line.split('|')
        left, right = int(left_str), int(right_str)

        if left in indegree and right in indegree:
            # if both pages are in this update, create edge left->right
            graph[left].append(right)
            indegree[right] += 1

    # find all nodes with indegree 0
    queue = deque([p for p in pages if indegree[p] == 0])

    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neigh in graph[node]:
            indegree[neigh] -= 1
            if indegree[neigh] == 0:
                queue.append(neigh)

    # order now should contain all pages in the correct order
    return order


def sum_rules(filename):
    lines = read_input(filename)
    rules, updates = parse_rules_and_updates(lines)

    correct_updates_middle_sum = 0
    incorrect_updates = []

    for update in updates:
        if check_update_order(update, rules):
            # correct update
            pages = [int(x.strip()) for x in update.split(',')]
            mid_page = pages[len(pages) // 2]
            correct_updates_middle_sum += mid_page
        else:
            # incorrect updates
            incorrect_updates.append(update)

    print("Correct Sum:", correct_updates_middle_sum)

    # for incorrect updates, reorder using topological sort and sum middle
    incorrect_updates_middle_sum = 0
    for update in incorrect_updates:
        pages = [int(x.strip()) for x in update.split(',')]
        correct_order = topological_sort(pages, rules)
        mid_page = correct_order[len(correct_order) // 2]
        incorrect_updates_middle_sum += mid_page

    print("Incorrect Sum:", incorrect_updates_middle_sum)


if __name__ == "__main__":
    main()