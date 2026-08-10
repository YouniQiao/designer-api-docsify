# isLocked（系统接口）

## 导入模块

```TypeScript
import { screenLock } from 'kits/@kit.BasicServicesKit';
```

## isLocked

```TypeScript
function isLocked(): boolean
```

Checks whether the screen is currently locked.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-screenLock-function isLocked(): boolean--><!--Device-screenLock-function isLocked(): boolean-End-->

**系统能力：** SystemCapability.MiscServices.ScreenLock

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | returns true if the screen is currently locked, returns false otherwise. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 202 | permission verification failed, application which is not a system application uses system API. |

## 示例

```TypeScript
let isLocked = screenLock.isLocked();
```

