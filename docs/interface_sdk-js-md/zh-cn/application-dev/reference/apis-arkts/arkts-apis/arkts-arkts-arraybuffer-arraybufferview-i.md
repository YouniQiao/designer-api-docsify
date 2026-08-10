# ArrayBufferView

Interface representing a view of an ArrayBuffer.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export interface ArrayBufferView--><!--Device-unnamed-export interface ArrayBufferView-End-->

**系统能力：** SystemCapability.Utils.Lang

## buffer

```TypeScript
readonly buffer: ArrayBuffer
```

The ArrayBuffer instance referenced by the array.

**类型：** ArrayBuffer

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBufferView-readonly buffer: ArrayBuffer--><!--Device-ArrayBufferView-readonly buffer: ArrayBuffer-End-->

**系统能力：** SystemCapability.Utils.Lang

## byteLength

```TypeScript
readonly byteLength: int
```

The length in bytes of the array.The value must be an integer greater than or equal to 0.

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBufferView-readonly byteLength: int--><!--Device-ArrayBufferView-readonly byteLength: int-End-->

**系统能力：** SystemCapability.Utils.Lang

## byteOffset

```TypeScript
readonly byteOffset: int
```

The offset in bytes of the array.The value must be an integer greater than or equal to 0.

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ArrayBufferView-readonly byteOffset: int--><!--Device-ArrayBufferView-readonly byteOffset: int-End-->

**系统能力：** SystemCapability.Utils.Lang

