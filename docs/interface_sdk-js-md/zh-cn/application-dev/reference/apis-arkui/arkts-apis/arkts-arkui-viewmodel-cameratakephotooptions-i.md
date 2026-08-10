# CameraTakePhotoOptions

CameraTakePhotoOptions

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

<!--Device-unnamed-export interface CameraTakePhotoOptions--><!--Device-unnamed-export interface CameraTakePhotoOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## complete

```TypeScript
complete?: (result: Object) => void
```

Callback function at the end of the interface invoking (executed both successfully and unsuccessfully).

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-CameraTakePhotoOptions-complete?: (result: Object) => void--><!--Device-CameraTakePhotoOptions-complete?: (result: Object) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | Object | 是 |  |

## fail

```TypeScript
fail?: (result: Object) => void
```

Callback function for interface invocation failure.

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-CameraTakePhotoOptions-fail?: (result: Object) => void--><!--Device-CameraTakePhotoOptions-fail?: (result: Object) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | Object | 是 |  |

## success

```TypeScript
success?: (result: Object) => void
```

Callback function for successful interface invocation.

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-CameraTakePhotoOptions-success?: (result: Object) => void--><!--Device-CameraTakePhotoOptions-success?: (result: Object) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | Object | 是 |  |

## quality

```TypeScript
quality: "high" | "normal" | "low"
```

Picture quality.

**类型：** "high" \| "normal" \| "low"

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-CameraTakePhotoOptions-quality: "high" | "normal" | "low"--><!--Device-CameraTakePhotoOptions-quality: "high" | "normal" | "low"-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

