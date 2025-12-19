def apply_cfd_boundaries(simulation, fusion_payload):
    """
    Applies CFD boundary conditions to an existing Fusion simulation study.
    """

    bc = fusion_payload["boundary_conditions"]

    velocity = bc["velocity_inlet_mps"]
    temperature = bc["inlet_temperature_k"]

    # ---- Get named faces from CAD ----
    inlet_face = simulation.find_face_by_name("INLET")
    outlet_face = simulation.find_face_by_name("OUTLET")

    # ---- Velocity Inlet ----
    simulation.create_velocity_inlet(
        face=inlet_face,
        velocity=velocity,
        temperature=temperature
    )

    # ---- Pressure Outlet ----
    simulation.create_pressure_outlet(
        face=outlet_face,
        pressure=0  # gauge pressure
    )

    print("[FUSION API] CFD boundaries applied successfully")
