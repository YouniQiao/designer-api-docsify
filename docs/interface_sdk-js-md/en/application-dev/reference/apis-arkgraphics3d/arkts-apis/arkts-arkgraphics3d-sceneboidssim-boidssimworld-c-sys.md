# BoidsSimWorld (System API)

The Boids simulation world object, used to manage the lifecycle and components of the Boids simulation. > **NOTE：**> Before using the following APIs, you need to obtain the Boids simulation world instance through BoidsSimPlugin.getDefaultBoidsSimWorld.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

<!--Device-unnamed-export declare class BoidsSimWorld--><!--Device-unnamed-export declare class BoidsSimWorld-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## addBoidsSimComponent

```TypeScript
addBoidsSimComponent(node: Node, param: BoidsSimParameters): void
```

Adds a flock behavior component at the specified node.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimWorld-addBoidsSimComponent(node: Node, param: BoidsSimParameters): void--><!--Device-BoidsSimWorld-addBoidsSimComponent(node: Node, param: BoidsSimParameters): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Yes | Node of the target scene. |
| param | [BoidsSimParameters](arkts-arkgraphics3d-sceneboidssim-boidssimparameters-i-sys.md) | Yes | Flock behavior parameters. |

## addBoidsSimGravityComponent

```TypeScript
addBoidsSimGravityComponent(node: Node, param: BoidsSimGravityParameters): void
```

Adds an attraction field component at the specified node.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimWorld-addBoidsSimGravityComponent(node: Node, param: BoidsSimGravityParameters): void--><!--Device-BoidsSimWorld-addBoidsSimGravityComponent(node: Node, param: BoidsSimGravityParameters): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Yes | Node of the target scene. |
| param | [BoidsSimGravityParameters](arkts-arkgraphics3d-sceneboidssim-boidssimgravityparameters-i-sys.md) | Yes | Attraction field parameters. |

## addBoidsSimRepulsionComponent

```TypeScript
addBoidsSimRepulsionComponent(node: Node, param: BoidsSimRepulsionParameters): void
```

Adds a repulsion field component at the specified node.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimWorld-addBoidsSimRepulsionComponent(node: Node, param: BoidsSimRepulsionParameters): void--><!--Device-BoidsSimWorld-addBoidsSimRepulsionComponent(node: Node, param: BoidsSimRepulsionParameters): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Yes | Node of the target scene. |
| param | [BoidsSimRepulsionParameters](arkts-arkgraphics3d-sceneboidssim-boidssimrepulsionparameters-i-sys.md) | Yes | Repulsion field parameters. |

## getBoidsSimComponent

```TypeScript
getBoidsSimComponent(node: Node): BoidsSimParameters | null
```

Gets the flock behavior parameters on the specified node.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimWorld-getBoidsSimComponent(node: Node): BoidsSimParameters | null--><!--Device-BoidsSimWorld-getBoidsSimComponent(node: Node): BoidsSimParameters | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Yes | Node of the target scene. |

**Return value:**

| Type | Description |
| --- | --- |
| [BoidsSimParameters](arkts-arkgraphics3d-sceneboidssim-boidssimparameters-i-sys.md) | Returns the flock behavior parameters, or null if the node does not have this component mounted. |

## getBoidsSimGravityComponent

```TypeScript
getBoidsSimGravityComponent(node: Node): BoidsSimGravityParameters | null
```

Gets the attraction field parameters on the specified node.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimWorld-getBoidsSimGravityComponent(node: Node): BoidsSimGravityParameters | null--><!--Device-BoidsSimWorld-getBoidsSimGravityComponent(node: Node): BoidsSimGravityParameters | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Yes | Node of the target scene. |

**Return value:**

| Type | Description |
| --- | --- |
| [BoidsSimGravityParameters](arkts-arkgraphics3d-sceneboidssim-boidssimgravityparameters-i-sys.md) | Returns the attraction field parameters, or null if the node does not have this component mounted. |

## getBoidsSimRepulsionComponent

```TypeScript
getBoidsSimRepulsionComponent(node: Node): BoidsSimRepulsionParameters | null
```

Gets the repulsion field parameters on the specified node.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimWorld-getBoidsSimRepulsionComponent(node: Node): BoidsSimRepulsionParameters | null--><!--Device-BoidsSimWorld-getBoidsSimRepulsionComponent(node: Node): BoidsSimRepulsionParameters | null-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Yes | Node of the target scene. |

**Return value:**

| Type | Description |
| --- | --- |
| [BoidsSimRepulsionParameters](arkts-arkgraphics3d-sceneboidssim-boidssimrepulsionparameters-i-sys.md) | Returns the repulsion field parameters, or null if the node does not have this component mounted. |

## pause

```TypeScript
pause(): void
```

Pauses the Boids simulation.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimWorld-pause(): void--><!--Device-BoidsSimWorld-pause(): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## play

```TypeScript
play(): void
```

Starts or resumes the Boids simulation.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimWorld-play(): void--><!--Device-BoidsSimWorld-play(): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

## removeBoidsSimComponent

```TypeScript
removeBoidsSimComponent(node: Node): void
```

Removes the flock behavior component from the specified node.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimWorld-removeBoidsSimComponent(node: Node): void--><!--Device-BoidsSimWorld-removeBoidsSimComponent(node: Node): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Yes | Node of the target scene. |

## removeBoidsSimGravityComponent

```TypeScript
removeBoidsSimGravityComponent(node: Node): void
```

Removes the attraction field component on the specified node.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimWorld-removeBoidsSimGravityComponent(node: Node): void--><!--Device-BoidsSimWorld-removeBoidsSimGravityComponent(node: Node): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Yes | Node of the target scene. |

## removeBoidsSimRepulsionComponent

```TypeScript
removeBoidsSimRepulsionComponent(node: Node): void
```

Removes the repulsion field component from the specified node.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimWorld-removeBoidsSimRepulsionComponent(node: Node): void--><!--Device-BoidsSimWorld-removeBoidsSimRepulsionComponent(node: Node): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Yes | Node of the target scene. |

## setBoidsSimComponent

```TypeScript
setBoidsSimComponent(node: Node, param: BoidsSimParameters): void
```

Updates the flock behavior component on the specified node.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimWorld-setBoidsSimComponent(node: Node, param: BoidsSimParameters): void--><!--Device-BoidsSimWorld-setBoidsSimComponent(node: Node, param: BoidsSimParameters): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Yes | Node of the target scene. |
| param | [BoidsSimParameters](arkts-arkgraphics3d-sceneboidssim-boidssimparameters-i-sys.md) | Yes | Flock behavior parameters. |

## setBoidsSimGravityComponent

```TypeScript
setBoidsSimGravityComponent(node: Node, param: BoidsSimGravityParameters): void
```

Updates the attraction field component on the specified node.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimWorld-setBoidsSimGravityComponent(node: Node, param: BoidsSimGravityParameters): void--><!--Device-BoidsSimWorld-setBoidsSimGravityComponent(node: Node, param: BoidsSimGravityParameters): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Yes | Node of the target scene. |
| param | [BoidsSimGravityParameters](arkts-arkgraphics3d-sceneboidssim-boidssimgravityparameters-i-sys.md) | Yes | Attraction field parameters. |

## setBoidsSimRepulsionComponent

```TypeScript
setBoidsSimRepulsionComponent(node: Node, param: BoidsSimRepulsionParameters): void
```

Updates the repulsion field component on the specified node.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimWorld-setBoidsSimRepulsionComponent(node: Node, param: BoidsSimRepulsionParameters): void--><!--Device-BoidsSimWorld-setBoidsSimRepulsionComponent(node: Node, param: BoidsSimRepulsionParameters): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [Node](arkts-arkgraphics3d-scenenodes-node-i.md) | Yes | Node of the target scene. |
| param | [BoidsSimRepulsionParameters](arkts-arkgraphics3d-sceneboidssim-boidssimrepulsionparameters-i-sys.md) | Yes | Repulsion field parameters. |

## stop

```TypeScript
stop(): void
```

Stops the Boids simulation and resets the state.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-BoidsSimWorld-stop(): void--><!--Device-BoidsSimWorld-stop(): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**System API:** This is a system API.

