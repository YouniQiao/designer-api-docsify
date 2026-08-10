# isScreenLocked

## 导入模块

```TypeScript
import { screenLock } from 'kits/@kit.BasicServicesKit';
```

## isScreenLocked

```TypeScript
function isScreenLocked(callback: AsyncCallback<boolean>): void
```

Checks whether the screen is currently locked.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**废弃版本：** 9

<!--Device-screenLock-function isScreenLocked(callback: AsyncCallback<boolean>): void--><!--Device-screenLock-function isScreenLocked(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.MiscServices.ScreenLock

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 | the callback of isScreenLocked. |

## 示例

```TypeScript
import { BusinessError } from '@ohos.base';

screenLock.isScreenLocked((err: BusinessError, data: Boolean)=>{      
  if (err) {
    console.error(`Failed to obtain whether the screen is locked, Code: ${err.code}, message: ${err.message}`);
    return;    
  }
  console.info(`Succeeded in Obtaining whether the screen is locked. result: ${data}`);
});
```


## isScreenLocked

```TypeScript
function isScreenLocked(): Promise<boolean>
```

Checks whether the screen is currently locked.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**废弃版本：** 9

<!--Device-screenLock-function isScreenLocked(): Promise<boolean>--><!--Device-screenLock-function isScreenLocked(): Promise<boolean>-End-->

**系统能力：** SystemCapability.MiscServices.ScreenLock

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;boolean&gt; | the promise returned by the function. |

## 示例

```TypeScript
import { BusinessError } from '@ohos.base';

screenLock.isScreenLocked().then((data: Boolean) => {
  console.info(`Succeeded in Obtaining whether the screen is locked. result: ${data}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to obtain whether the screen is locked, Code: ${err.code}, message: ${err.message}`);
});
```

