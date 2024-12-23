use super::*;

pub fn run() {
    let mut trajectories = Vec::new();

    for line in get_input("day24.txt").lines().map(expect_line) {
        let (position, velocity) = line.split_once(" @ ").unwrap();

        let mut position = position.split(", ");
        let position = FPoint3D(
            position.next().unwrap().parse::<f64>().unwrap(),
            position.next().unwrap().parse::<f64>().unwrap(),
            position.next().unwrap().parse::<f64>().unwrap(),
        );

        let mut velocity = velocity.split(", ");
        let velocity = FPoint3D(
            velocity.next().unwrap().parse::<f64>().unwrap(),
            velocity.next().unwrap().parse::<f64>().unwrap(),
            velocity.next().unwrap().parse::<f64>().unwrap(),
        );

        trajectories.push((position, velocity));
    }

    let mut collided_xy: u64 = 0;

    for (index, &(FPoint3D(x1, y1, z1), FPoint3D(dx1, dy1, dz1))) in trajectories.iter().enumerate() {
        for &(FPoint3D(x2, y2, _z2), FPoint3D(dx2, dy2, _dz2)) in trajectories[index + 1 ..].iter() {
            if dx2 * dy1 != dx1 * dy2 {
                let t = (dx2 * (y2 - y1) - dy2 * (x2 - x1)) / (dx2 * dy1 - dx1 * dy2);
                let s = (dx1 * (y2 - y1) - dy1 * (x2 - x1)) / (dx2 * dy1 - dx1 * dy2);
                let cx = x1 + dx1 * t;
                let cy = y1 + dy1 * t;
                if t > 0.0 && s > 0.0 && 2e14 <= cx && cx <= 4e14 && 2e14 <= cy && cy <= 4e14 {
                    collided_xy += 1;
                }
            }
        }
    }

    println!("[24p1] {collided_xy}");

    let mut trajectories = Vec::new();

    for line in get_input("day24.txt").lines().map(expect_line) {
        let (position, velocity) = line.split_once(" @ ").unwrap();

        let mut position = position.split(", ");
        let position = Point3D(
            position.next().unwrap().parse::<i64>().unwrap(),
            position.next().unwrap().parse::<i64>().unwrap(),
            position.next().unwrap().parse::<i64>().unwrap(),
        );

        let mut velocity = velocity.split(", ");
        let velocity = Point3D(
            velocity.next().unwrap().parse::<i64>().unwrap(),
            velocity.next().unwrap().parse::<i64>().unwrap(),
            velocity.next().unwrap().parse::<i64>().unwrap(),
        );

        trajectories.push((position, velocity));
    }

    let mut x_velocities: BTreeMap<i64, Vec<usize>> = BTreeMap::new();
    let mut y_velocities: BTreeMap<i64, Vec<usize>> = BTreeMap::new();
    let mut z_velocities: BTreeMap<i64, Vec<usize>> = BTreeMap::new();

    for (index, (position, velocity)) in trajectories.iter().enumerate() {
        if let Some(indices) = x_velocities.get_mut(&velocity.x()) {
            indices.push(index);
        }
        else {
            x_velocities.insert(velocity.x(), Vec::new());
        }
        if let Some(indices) = y_velocities.get_mut(&velocity.y()) {
            indices.push(index);
        }
        else {
            y_velocities.insert(velocity.y(), Vec::new());
        }
        if let Some(indices) = z_velocities.get_mut(&velocity.z()) {
            indices.push(index);
        }
        else {
            z_velocities.insert(velocity.z(), Vec::new());
        }
    }
    
    // fn x(point: Point3D) -> i64 {
    //     point.x()
    // }
    // fn y(point: Point3D) -> i64 {
    //     point.y()
    // }

    for (&x_vel, indices) in &x_velocities {
        // if indices.len() < 3 {
        //     continue;
        // }
        if indices.len() < 2 {
            continue;
        }
        for &index in indices {
            println!("{:?}", trajectories[index]);
        }
        for &index1 in indices {
            for &index2 in indices {
                // if index2 == index1 {
                //     continue;
                // }
                if index2 <= index1 {
                    continue;
                }
                let (pos1, vel1) = trajectories[index1];
                let (pos2, vel1) = trajectories[index2];
                // for &index3 in indices {
                //     if index3 == index2 || index3 == index1 {
                //         continue;
                //     }
                //     let (pos1, vel1) = trajectories[index1];
                //     let (pos2, vel2) = trajectories[index2];
                //     let (pos3, vel3) = trajectories[index3];
                //     let x21 = x(pos2) - x(pos1);
                //     let x13 = x(pos1) - x(pos3);
                //     let x23 = x(pos2) - x(pos3);
                //     let gcd1 = gcd(x21.unsigned_abs(), x13.unsigned_abs());
                //     let gcd2 = gcd(x13.unsigned_abs(), x23.unsigned_abs());
                //     let gcd3 = gcd(x23.unsigned_abs(), x21.unsigned_abs());
                //     let divisor = gcd1.min(gcd2).min(gcd3) as i64;
                //     let x21 = x21 / divisor;
                //     let x13 = x13 / divisor;
                //     let x23 = x23 / divisor;
                //     for t3_factor in -10000..=10000 {
                //         for t2_factor in -10000..=10000 {
                //             if t2_factor == t3_factor {
                //                 continue;
                //             }
                //             let t1 = (x21 * t3_factor + x13 * t2_factor) as i128;
                //             let t2 = (t2_factor * x23) as i128;
                //             let t3 = (t3_factor * x23) as i128;
                //             if t1 <= 0 || t2 <= 0 || t3 <= 0 {
                //                 continue;
                //             }
                //             // (y2-y3)*t1 + (y3-y1)*t2 + (y1-y2)*t3 + (v3-v2)*t2*t3 + (v1-v3)*t1*t3 + (v2-v1)*t1*t2 = 0
                //             let y23 = (y(pos2) - y(pos3)) as i128;
                //             let y31 = (y(pos3) - y(pos1)) as i128;
                //             let y12 = (y(pos1) - y(pos2)) as i128;
                //             let v32 = (y(vel3) - y(vel2)) as i128;
                //             let v13 = (y(vel1) - y(vel3)) as i128;
                //             let v21 = (y(vel2) - y(vel1)) as i128;
                //             let test = (y23 * t1) + (y31 * t2) + (y12 * t3) + (v32 * t3 * t2) + (v13 * t1 * t3) + (v21 * t2 * t1);
                //             if test == 0 {
                //                 println!("{t1} {t2} {t3}");
                //             }
                //         }
                //     }
                // }
            }
        }
    }

    // let mut trajectories = Vec::from_iter(trajectories.iter()
    //     .map(|&(FPoint3D(x, y, z), FPoint3D(dx, dy, dz))| (Point3D(x as i64, y as i64, z as i64), Point3D(dx as i64, dy as i64, dz as i64))));
    // trajectories.sort_unstable_by_key(|(_, velocity)| velocity.manhattan_distance_to(Point3D::origin()));
    // let (position_1, velocity_1) = trajectories[trajectories.len() - 1];
    // let (position_2, velocity_2) = trajectories[trajectories.len() - 2];

    // let mut t1 = 1;
    // let mut t2 = 0;
    
    // let rock_position = 'search_loop: loop {
    //     for (t1, t2) in [(t1, t2), (t2, t1)] {
    //         let dt = t2 - t1;
    //         let x1 = position_1.x() as i128 + velocity_1.x() as i128 * t1;
    //         let y1 = position_1.y() as i128 + velocity_1.y() as i128 * t1;
    //         let z1 = position_1.z() as i128 + velocity_1.z() as i128 * t1;
    //         let x2 = position_2.x() as i128 + velocity_2.x() as i128 * t2;
    //         let y2 = position_2.y() as i128 + velocity_2.y() as i128 * t2;
    //         let z2 = position_2.z() as i128 + velocity_2.z() as i128 * t2;

    //         // println!("{t1}, {t2} : {}", trajectories.iter().map(|&(position, velocity)| (x2 - x1 - velocity.x() as i128 * dt) * (y2 * t1 - y1 * t2 + position.y() as i128 * dt) - (y2 - y1 - velocity.y() as i128 * dt) * (x2 * t1 - x1 * t2 + position.x() as i128 * dt)).sum::<i128>());

    //         if trajectories.iter().all(|&(position, velocity)| {
    //             (x2 - x1 - velocity.x() as i128 * dt) * (y2 * t1 - y1 * t2 + position.y() as i128 * dt)
    //             == (y2 - y1 - velocity.y() as i128 * dt) * (x2 * t1 - x1 * t2 + position.x() as i128 * dt)
    //         }) {
    //             let rock_position = Point3D(
    //                 ((x1 * t2 - x2 * t1) / dt) as i64,
    //                 ((y1 * t2 - y2 * t1) / dt) as i64,
    //                 ((z1 * t2 - z2 * t1) / dt) as i64,
    //             );
    //             break 'search_loop rock_position;
    //         }
    //     }

    //     if t2 == 0 {
    //         t2 = t1;
    //         t1 += 1;
    //     }
    //     else {
    //         t2 -= 1;
    //     }
    // };

    // let coordinate_sum = rock_position.manhattan_distance_to(Point3D::origin());
    // println!("[24p2] Rock starting position: {rock_position} => {coordinate_sum}")
}
