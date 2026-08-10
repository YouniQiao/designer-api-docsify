# Constants

## APPEND

```TypeScript
const APPEND: int
```

以追加方式打开，后续写将追加到文件末尾。值为 0o2000。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OpenMode-const APPEND: int--><!--Device-OpenMode-const APPEND: int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## CREATE

```TypeScript
const CREATE: int
```

若文件不存在，则创建文件。值为 0o100。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OpenMode-const CREATE: int--><!--Device-OpenMode-const CREATE: int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## DIR

```TypeScript
const DIR: int
```

如果path不指向目录，则出错。值为 0o200000。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OpenMode-const DIR: int--><!--Device-OpenMode-const DIR: int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## NOFOLLOW

```TypeScript
const NOFOLLOW: int
```

如果path指向符号链接，则出错。值为 0o400000。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OpenMode-const NOFOLLOW: int--><!--Device-OpenMode-const NOFOLLOW: int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## NONBLOCK

```TypeScript
const NONBLOCK: int
```

如果path指向FIFO、块特殊文件或字符特殊文件，则本次打开及后续 IO 进行非阻塞操作。值为 0o4000。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OpenMode-const NONBLOCK: int--><!--Device-OpenMode-const NONBLOCK: int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## READ_ONLY

```TypeScript
const READ_ONLY: int
```

只读打开。值为 0o0。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OpenMode-const READ_ONLY: int--><!--Device-OpenMode-const READ_ONLY: int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## READ_WRITE

```TypeScript
const READ_WRITE: int
```

读写打开。值为 0o2。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OpenMode-const READ_WRITE: int--><!--Device-OpenMode-const READ_WRITE: int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## SYNC

```TypeScript
const SYNC: int
```

以同步IO的方式打开文件。值为 0o4010000。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OpenMode-const SYNC: int--><!--Device-OpenMode-const SYNC: int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## TRUNC

```TypeScript
const TRUNC: int
```

如果文件存在且以只写或读写的方式打开，则将其长度裁剪为零。值为 0o1000

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OpenMode-const TRUNC: int--><!--Device-OpenMode-const TRUNC: int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## UNCACHE

```TypeScript
const UNCACHE: int
```

读写文件不进行页缓存。值为 0o10000000000。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OpenMode-const UNCACHE: int--><!--Device-OpenMode-const UNCACHE: int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## WRITE_ONLY

```TypeScript
const WRITE_ONLY: int
```

只写打开。值为 0o1。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-OpenMode-const WRITE_ONLY: int--><!--Device-OpenMode-const WRITE_ONLY: int-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

