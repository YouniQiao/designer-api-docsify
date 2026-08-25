# Animation

Animation resource, which inherits from SceneResource.@extends SceneResource @interface Animation

**Inheritance/Implementation:** Animation extends [SceneResource](arkts-arkgraphics3d-sceneresources-sceneresource-i.md)

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## finish

```TypeScript
finish(): void
```

Finishes the playing of the animation and sets its progress of 1 (finished).

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## onFinished

```TypeScript
onFinished(callback: Callback<void>): void
```

Called when the animation playback is complete or the finish API is called.

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

## onStarted

```TypeScript
onStarted(callback: Callback<void>): void
```

Called when the animation starts to play. The start operation is triggered by calling start or restart.

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

## pause

```TypeScript
pause(): void
```

Pauses the animation. The animation remains in the current playing progress.

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## restart

```TypeScript
restart(): void
```

Plays the animation from the beginning.

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## seek

```TypeScript
seek(position: number): void
```

Plays the animation from the specified position.

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| position | number | Yes |

## start

```TypeScript
start(): void
```

Plays the animation based on the current progress.

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## stop

```TypeScript
stop(): void
```

Stops playing the animation and sets its progress to 0 (not started).

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## duration

```TypeScript
readonly duration: number
```

Animation duration, in seconds. The value must be greater than or equal to 0.

**Type:** number

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## enabled

```TypeScript
enabled: boolean
```

Whether the animation is enabled. true if enabled, false otherwise.

**Type:** boolean

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## progress

```TypeScript
readonly progress: number
```

Playing progress of the animation. The value range is [0, 1].

**Type:** number

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## running

```TypeScript
readonly running: boolean
```

Whether the animation is running. true if running, false otherwise.

**Type:** boolean

**Since:** 12

**System capability:** SystemCapability.ArkUi.Graphics3D

## speed

```TypeScript
speed?: number
```

Playback speed factor of the animation. The default value is 1.0, indicating that the animation is played at normal speed. If the value is negative, the animation plays in reverse.

**Type:** number

**Since:** 20

**System capability:** SystemCapability.ArkUi.Graphics3D
