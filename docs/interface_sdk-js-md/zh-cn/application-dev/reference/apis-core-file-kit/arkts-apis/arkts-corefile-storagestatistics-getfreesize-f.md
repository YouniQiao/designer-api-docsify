# getFreeSize

## 导入模块

```TypeScript
import { storageStatistics } from '@kit.CoreFileKit';
```

## getFreeSize

```TypeScript
function getFreeSize(callback: AsyncCallback<long>): void
```

获取内置存储的可用空间大小（单位为Byte），以callback方式返回。

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** 
- API版本9 - 14：ohos.permission.STORAGE_MANAGER

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | ArkTS-Dyn: [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt;  <br>ArkTS-Sta：[AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13600001 |
| 13900042 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

storageStatistics.getFreeSize().then((freeSize: number) => {
  console.info('getFreeSize successfully:' + freeSize);
}).catch((err: BusinessError) => {
  console.error(`getFreeSize failed. Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let totalSize: long = 0;
storageStatistics.getFreeSize().then((freeSize) => {
  console.info('getFreeSize successfully:' + freeSize);
}).catch((err: BusinessError): void => {
  console.error(`getFreeSize failed. Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

storageStatistics.getFreeSize((error: BusinessError, freeSize: number) => {
  if (error) {
    console.error(`getFreeSize failed. Code: ${error.code}, message: ${error.message}`);
  } else {
    // do something
    console.info('getFreeSize successfully:' + freeSize);
  }
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let error: BusinessError = {};
let totalSize: long = 0;
storageStatistics.getFreeSize((error, freeSize): void => {
  if (error) {
    console.error(`getFreeSize failed. Code: ${error.code}, message: ${error.message}`);
  } else {
    // do something
    console.info('getFreeSize successfully:' + freeSize);
  }
});
```


## getFreeSize

```TypeScript
function getFreeSize(): Promise<long>
```

获取内置存储的可用空间大小（单位为Byte），以Promise方式返回。

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** 
- API版本9 - 14：ohos.permission.STORAGE_MANAGER

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: Promise & lt;number & gt;<br>ArkTS-Sta：Promise & lt;long & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| 13600001 |
| 13900042 |

**示例**

参见 [getFreeSize](#getfreesize)
