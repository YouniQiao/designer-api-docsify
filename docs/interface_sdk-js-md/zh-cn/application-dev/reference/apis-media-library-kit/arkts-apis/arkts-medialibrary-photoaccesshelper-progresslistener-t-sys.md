# ProgressListener（系统接口）

```TypeScript
type ProgressListener = (progress: Progress) => void
```

Indicates the type of the progress of batch operation.

Progress callback, which can be the size or numberof files.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-photoAccessHelper-type ProgressListener = (progress: Progress) => void--><!--Device-photoAccessHelper-type ProgressListener = (progress: Progress) => void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| progress | [Progress](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-progress-i.md) | 是 | progress info. |

