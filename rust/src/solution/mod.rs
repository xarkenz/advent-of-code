pub mod day01;

use crate::utils::*;

use std::io::BufRead;
use std::time::Instant;
use std::collections::{
    BTreeMap,
    HashMap,
    BTreeSet,
    HashSet,
    VecDeque,
    BinaryHeap,
};

pub fn get_input(name: &'static str) -> std::io::BufReader<std::fs::File> {
    std::io::BufReader::new(std::fs::File::open(format!("../input/{name}"))
        .expect("unable to open input file"))
}

pub fn expect_line(result: std::io::Result<String>) -> String {
    result.expect("error while reading input file")
}

pub fn expect_bytes(result: std::io::Result<Vec<u8>>) -> Vec<u8> {
    result.expect("error while reading input file")
}

pub fn print_elapsed_time(label: &str, since: Instant) {
    println!("\x1b[2m{label}: {} ms\x1b[22m", since.elapsed().as_millis());
}
