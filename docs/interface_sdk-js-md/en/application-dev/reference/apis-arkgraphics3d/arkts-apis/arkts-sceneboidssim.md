# SceneBoidsSim

## Summary

<!--Del-->
### Classes(System API)

| Name | Description |
| --- | --- |
| [BoidsSimPlugin](arkts-arkgraphics3d-sceneboidssim-boidssimplugin-c-sys.md) | Boids simulation plugin, providing static methods for obtaining the boids simulation world. |
| [BoidsSimWorld](arkts-arkgraphics3d-sceneboidssim-boidssimworld-c-sys.md) | The Boids simulation world object, used to manage the lifecycle and components of the Boids simulation. > **NOTE：**> > Before using the following APIs, you need to obtain the Boids simulation world instance through [getDefaultBoidsSimWorld](arkts-arkgraphics3d-sceneboidssim-boidssimplugin-c-sys.md#getdefaultboidssimworld). |
<!--DelEnd-->

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [BoidsSimGravityParameters](arkts-arkgraphics3d-sceneboidssim-boidssimgravityparameters-i-sys.md) | Attraction field parameters, used to configure the attraction field in the scene. |
| [BoidsSimParameters](arkts-arkgraphics3d-sceneboidssim-boidssimparameters-i-sys.md) | Boids simulation parameters used to configure the behavioral attributes of each individual. > **NOTE：**> > A simulation frame refers to the update cycle executed at a fixed time step in the Boids simulation, similar to FixedUpdate in Unity. > The default time step is 16 ms (approximately 62.5 FPS). The simulation is driven by accumulating real time and consuming it in fixed steps. > The default values of some parameters below are calculated based on this time step: > - maxVelocityMag: 0.01 / 0.016 ≈ 0.625 (m/s). > - maxAccelerationMag: maxVelocityMag / 0.016 ≈ 39.06 (m/s²). > - maxTurnRate: π × 0.75 × 0.016 ≈ 0.0377 (rad/simulation frame). |
| [BoidsSimRepulsionParameters](arkts-arkgraphics3d-sceneboidssim-boidssimrepulsionparameters-i-sys.md) | Repulsion field parameters, used to configure the repulsion field in the scene. |
<!--DelEnd-->

