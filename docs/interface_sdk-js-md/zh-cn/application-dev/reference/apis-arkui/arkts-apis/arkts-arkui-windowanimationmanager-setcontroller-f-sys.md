# setController（系统接口）

## 导入模块

```TypeScript
import { windowAnimationManager } from 'kits/@kit.ArkUI';
```

## setController

```TypeScript
function setController(controller: WindowAnimationController): void
```

设置窗口动画控制器。窗口动画控制器的说明请参考[WindowAnimationController](arkts-arkui-windowanimationmanager-windowanimationcontroller-i-sys.md)。在使用windowAnimationManager的其他接口前，需要预先调用本接口设置窗口动画控制器。

**起始版本：** 9

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| controller | [WindowAnimationController](arkts-arkui-windowanimationmanager-windowanimationcontroller-i-sys.md) | 是 |
