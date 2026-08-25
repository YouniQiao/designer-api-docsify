# getCurrentBundleInodes

## 导入模块

```TypeScript
import { storageStatistics } from '@kit.CoreFileKit';
```

## getCurrentBundleInodes

```TypeScript
function getCurrentBundleInodes(): Promise<long>
```

获取当前应用的inode占用量，使用Promise异步回调。

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.FileManagement.StorageService.SpatialStatistics

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: Promise & lt;number & gt;<br>ArkTS-Sta：Promise & lt;long & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13600001 |
| 13600002 |
| 13600017 |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

storageStatistics.getCurrentBundleInodes().then((curInodes: number) => {
  console.info('getCurrentBundleInodes successfully:' + curInodes);
}).catch((err: BusinessError) => {
  console.error(`getCurrentBundleInodes failed. Code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

storageStatistics.getCurrentBundleInodes().then((curInodes: long) => {
  console.info('getCurrentBundleInodes successfully:' + curInodes);
}).catch((err: BusinessError): void => {
  console.error(`getCurrentBundleInodes failed. Code: ${err.code}, message: ${err.message}`);
});
```
