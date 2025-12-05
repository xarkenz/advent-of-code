#![allow(unused_imports)]
#![allow(unused_variables)]
#![allow(dead_code)]

use utils::*;

pub mod day01;

fn main() {
    let start_time = std::time::Instant::now();

    day01::run();

    print_elapsed_time("Total runtime", start_time);
}
