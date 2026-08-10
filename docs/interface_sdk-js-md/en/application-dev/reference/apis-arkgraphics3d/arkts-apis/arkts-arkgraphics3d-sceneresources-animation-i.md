# Animation

动画资源.

**Inheritance/Implementation:** Animation extends [SceneResource](arkts-arkgraphics3d-sceneresources-sceneresource-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface Animation extends SceneResource--><!--Device-unnamed-export interface Animation extends SceneResource-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## finish

```TypeScript
finish(): void
```

结束动画并将位置设置到结尾.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Animation-finish(): void--><!--Device-Animation-finish(): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## onFinished

```TypeScript
onFinished(callback: Callback<void>): void
```

动画播放结束时执行的回调函数，动画播放完成或者finish操作会触发这个回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Animation-onFinished(callback: Callback<void>): void--><!--Device-Animation-onFinished(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | 动画完成时调用的回调 |

## onStarted

```TypeScript
onStarted(callback: Callback<void>): void
```

注册动画开始时的回调.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Animation-onStarted(callback: Callback<void>): void--><!--Device-Animation-onStarted(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | 动画开始时调用的回调 |

## pause

```TypeScript
pause(): void
```

暂停动画.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Animation-pause(): void--><!--Device-Animation-pause(): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## restart

```TypeScript
restart(): void
```

重新启动动画.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Animation-restart(): void--><!--Device-Animation-restart(): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## seek

ArkTS-Dyn:
```TypeScript
seek(position: number): void
```

ArkTS-Sta:
```TypeScript
seek(position: double): void
```

将动画跳转到指定位置.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Animation-seek(position: double): void--><!--Device-Animation-seek(position: double): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| position | ArkTS-Dyn: number  <br>ArkTS-Sta：double | Yes | 跳转到0~1之间的位置 |

## start

```TypeScript
start(): void
```

开始动画.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Animation-start(): void--><!--Device-Animation-start(): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## stop

```TypeScript
stop(): void
```

停止动画并将位置设置到开头.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Animation-stop(): void--><!--Device-Animation-stop(): void-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## duration

```TypeScript
readonly duration: double
```

动画持续时间, 单位为秒.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Animation-readonly duration: double--><!--Device-Animation-readonly duration: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## enabled

```TypeScript
enabled: boolean
```

动画是否启用.

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Animation-enabled: boolean--><!--Device-Animation-enabled: boolean-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## progress

```TypeScript
readonly progress: double
```

动画在0~1之间的进度.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Animation-readonly progress: double--><!--Device-Animation-readonly progress: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## running

```TypeScript
readonly running: boolean
```

动画是否正在运行.

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-Animation-readonly running: boolean--><!--Device-Animation-readonly running: boolean-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

## speed

```TypeScript
speed?: double
```

动画速度因子负值使用给定速度因子反向播放动画

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-Animation-speed?: double--><!--Device-Animation-speed?: double-End-->

**System capability:** SystemCapability.ArkUi.Graphics3D

