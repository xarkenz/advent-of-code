use super::*;

pub fn run() {
    let lines = get_input("day01.txt").lines()
        .map(expect_line);

    let mut left_list: Vec<u32> = Vec::new();
    let mut right_list: Vec<u32> = Vec::new();

    for line in lines {
        let mut split = line.split_ascii_whitespace();
        left_list.push(split.next().unwrap().parse().unwrap());
        right_list.push(split.next().unwrap().parse().unwrap());
    }

    left_list.sort_unstable();
    right_list.sort_unstable();

    let total_distance: u32 = std::iter::zip(&left_list, &right_list)
        .map(|(&left, &right)| left.abs_diff(right))
        .sum();
    println!("[day01p1] Total distance: {total_distance}");

    let similarity_score: u32 = left_list.iter()
        .map(|&left| left * right_list.iter().filter(|&right| *right == left).count() as u32)
        .sum();
    println!("[day01p2] Similarity score: {similarity_score}");
}
