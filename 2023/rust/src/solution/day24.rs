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

    println!("[24p1] Intersecting trajectories: {collided_xy}");

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

    x_velocities.retain(|_, indices| indices.len() > 1);
    y_velocities.retain(|_, indices| indices.len() > 1);
    z_velocities.retain(|_, indices| indices.len() > 1);

    let mut x_vel_options = Vec::new();
    let mut y_vel_options = Vec::new();
    let mut z_vel_options = Vec::new();

    let components: [(_, _, fn(&Point3D) -> i64); 3] = [
        (&x_velocities, &mut x_vel_options, Point3D::x),
        (&y_velocities, &mut y_vel_options, Point3D::y),
        (&z_velocities, &mut z_vel_options, Point3D::z),
    ];
    for (velocities, vel_options, get_component) in components {
        for (&vel, indices) in velocities {
            for &index1 in indices {
                for &index2 in indices {
                    if index2 <= index1 {
                        continue;
                    }
                    let (pos1, _) = trajectories[index1];
                    let (pos2, _) = trajectories[index2];
                    let pos1 = get_component(&pos1);
                    let pos2 = get_component(&pos2);
                    if vel_options.is_empty() {
                        vel_options.extend((-1000..=1000).filter(|&vel_option| vel_option != vel && (pos2 - pos1) % (vel_option - vel) == 0));
                    }
                    else {
                        vel_options.retain(|&vel_option| vel_option != vel && (pos2 - pos1) % (vel_option - vel) == 0);
                    }
                }
            }
        }
    }

    let rock_velocity = Point3D(x_vel_options[0], y_vel_options[0], z_vel_options[0]);
    let (pos1, vel1) = trajectories[0];
    let (pos2, vel2) = trajectories[1];
    let x_vel_diff = vel1.x() - rock_velocity.x();
    let y_vel_diff = vel1.y() - rock_velocity.y();
    let numerator = (pos2.y() - pos1.y()) * x_vel_diff - (pos2.x() - pos1.x()) * y_vel_diff;
    let denominator = (rock_velocity.y() - vel2.y()) * x_vel_diff - (rock_velocity.x() - vel2.x()) * y_vel_diff;
    if numerator % denominator != 0 {
        println!("incorrect rock velocity: {rock_velocity}");
        return;
    }
    let time2 = numerator / denominator;
    let rock_position = pos2 - (rock_velocity - vel2) * time2;
    let coordinate_sum = rock_position.manhattan_distance_to(Point3D::origin());
    println!("[24p2] Rock starting position: {rock_position} -> {coordinate_sum}")
}
