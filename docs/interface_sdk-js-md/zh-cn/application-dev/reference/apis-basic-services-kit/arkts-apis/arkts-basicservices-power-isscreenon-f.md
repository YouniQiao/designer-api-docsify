# isScreenOn

## 导入模块

```TypeScript
import { power } from 'kits/@kit.BasicServicesKit';
```

## isScreenOn

```TypeScript
function isScreenOn(callback: AsyncCallback<boolean>): void
```

检测当前设备的亮灭屏状态。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [isActive](arkts-basicservices-power-isactive-f.md)

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |


## isScreenOn

```TypeScript
function isScreenOn(): Promise<boolean>
```

检测当前设备的亮灭屏状态。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [isActive](arkts-basicservices-power-isactive-f.md)

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |
