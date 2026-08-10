# BatchOperationOptions（系统接口）

Batch operation options

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

<!--Device-photoAccessHelper-interface BatchOperationOptions--><!--Device-photoAccessHelper-interface BatchOperationOptions-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## countProgressListener

```TypeScript
countProgressListener?: ProgressListener
```

count progress of batch operations.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BatchOperationOptions-countProgressListener?: ProgressListener--><!--Device-BatchOperationOptions-countProgressListener?: ProgressListener-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## resultListener

```TypeScript
resultListener?: ResultListener
```

the result of batch operations.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BatchOperationOptions-resultListener?: ResultListener--><!--Device-BatchOperationOptions-resultListener?: ResultListener-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## sizeProgressListener

```TypeScript
sizeProgressListener?: ProgressListener
```

size progress of batch operations.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BatchOperationOptions-sizeProgressListener?: ProgressListener--><!--Device-BatchOperationOptions-sizeProgressListener?: ProgressListener-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## mode

```TypeScript
mode?: int
```

the mode of Automatic renaming.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BatchOperationOptions-mode?: int--><!--Device-BatchOperationOptions-mode?: int-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## taskSignal

```TypeScript
taskSignal?: TaskSignal
```

interrupting of batch operations.

**类型：** [TaskSignal](../../apis-core-file-kit/arkts-apis/arkts-corefile-fileio-tasksignal-c.md)

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-BatchOperationOptions-taskSignal?: TaskSignal--><!--Device-BatchOperationOptions-taskSignal?: TaskSignal-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

