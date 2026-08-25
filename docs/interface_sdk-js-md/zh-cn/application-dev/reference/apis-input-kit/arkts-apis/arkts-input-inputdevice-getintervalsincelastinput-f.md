# getIntervalSinceLastInput

## 导入模块

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## getIntervalSinceLastInput

```TypeScript
function getIntervalSinceLastInput(): Promise<number>
```

获取距离上次系统输入事件的时间间隔（包含设备休眠时间），使用Promise异步回调。

**起始版本：** 14

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |
