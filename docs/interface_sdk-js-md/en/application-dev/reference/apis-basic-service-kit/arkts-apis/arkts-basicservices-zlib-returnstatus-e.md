# ReturnStatus

压缩/解压缩函数的返回代码。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-zlib-export enum ReturnStatus--><!--Device-zlib-export enum ReturnStatus-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## OK

```TypeScript
OK = 0
```

函数调用成功。该接口支持在原子化服务中使用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ReturnStatus-OK = 0--><!--Device-ReturnStatus-OK = 0-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## STREAM_END

```TypeScript
STREAM_END = 1
```

函数调用成功，表示已处理了整个数据。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ReturnStatus-STREAM_END = 1--><!--Device-ReturnStatus-STREAM_END = 1-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## NEED_DICT

```TypeScript
NEED_DICT = 2
```

函数调用成功，表示需要预设字典才能继续解压缩。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ReturnStatus-NEED_DICT = 2--><!--Device-ReturnStatus-NEED_DICT = 2-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## ERRNO

```TypeScript
ERRNO = -1
```

函数调用失败，表示文件操作错误。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ReturnStatus-ERRNO = -1--><!--Device-ReturnStatus-ERRNO = -1-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## STREAM_ERROR

```TypeScript
STREAM_ERROR = -2
```

函数调用失败，表示压缩或解压缩流错误。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ReturnStatus-STREAM_ERROR = -2--><!--Device-ReturnStatus-STREAM_ERROR = -2-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## DATA_ERROR

```TypeScript
DATA_ERROR = -3
```

函数调用失败，表示输入数据不正确。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ReturnStatus-DATA_ERROR = -3--><!--Device-ReturnStatus-DATA_ERROR = -3-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## MEM_ERROR

```TypeScript
MEM_ERROR = -4
```

函数调用失败，表示内存分配失败。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ReturnStatus-MEM_ERROR = -4--><!--Device-ReturnStatus-MEM_ERROR = -4-End-->

**System capability:** SystemCapability.BundleManager.Zlib

## BUF_ERROR

```TypeScript
BUF_ERROR = -5
```

函数调用失败，表示输入缓冲区不正确。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-ReturnStatus-BUF_ERROR = -5--><!--Device-ReturnStatus-BUF_ERROR = -5-End-->

**System capability:** SystemCapability.BundleManager.Zlib

