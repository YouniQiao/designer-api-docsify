# InputDeviceData

描述输入设备的信息。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-inputDevice-interface InputDeviceData--><!--Device-inputDevice-interface InputDeviceData-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

## Modules to Import

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## axisRanges

```TypeScript
axisRanges: Array<AxisRange>
```

输入设备的轴信息。

**Type:** Array&lt;AxisRange&gt;

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-InputDeviceData-axisRanges: Array<AxisRange>--><!--Device-InputDeviceData-axisRanges: Array<AxisRange>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

## bus

```TypeScript
bus: int
```

输入设备的总线类型，该值以输入设备上报为准。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputDeviceData-bus: int--><!--Device-InputDeviceData-bus: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

## id

```TypeScript
id: int
```

输入设备的唯一标识，同一个物理设备反复插拔，设备ID可能会发生变化。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-InputDeviceData-id: int--><!--Device-InputDeviceData-id: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

## isLocal

```TypeScript
isLocal?: boolean
```

输入设备是否为本地设备。

true表示是本地设备，false表示是非本地设备。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-InputDeviceData-isLocal?: boolean--><!--Device-InputDeviceData-isLocal?: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

## isVirtual

```TypeScript
isVirtual?: boolean
```

输入设备是否为虚拟设备。

true表示是虚拟设备，false表示是非虚拟设备。

**Type:** boolean

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-InputDeviceData-isVirtual?: boolean--><!--Device-InputDeviceData-isVirtual?: boolean-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

## name

```TypeScript
name: string
```

输入设备的名称。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-InputDeviceData-name: string--><!--Device-InputDeviceData-name: string-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

## phys

```TypeScript
phys: string
```

输入设备的物理地址。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputDeviceData-phys: string--><!--Device-InputDeviceData-phys: string-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

## product

```TypeScript
product: int
```

输入设备的产品信息。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputDeviceData-product: int--><!--Device-InputDeviceData-product: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

## sources

```TypeScript
sources: Array<SourceType>
```

输入设备的输入能力。包括键盘、鼠标、触摸屏、轨迹球、触控板、操纵杆等。

**Type:** Array&lt;SourceType&gt;

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-InputDeviceData-sources: Array<SourceType>--><!--Device-InputDeviceData-sources: Array<SourceType>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

## uniq

```TypeScript
uniq: string
```

输入设备的唯一标识。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputDeviceData-uniq: string--><!--Device-InputDeviceData-uniq: string-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

## vendor

```TypeScript
vendor: int
```

输入设备的厂商信息。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputDeviceData-vendor: int--><!--Device-InputDeviceData-vendor: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

## version

```TypeScript
version: int
```

输入设备的版本信息。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-InputDeviceData-version: int--><!--Device-InputDeviceData-version: int-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputDevice

