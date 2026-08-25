# end（系统接口）

## 导入模块

```TypeScript
import { performanceMonitor } from 'kits/@kit.ArkUI';
```

## end

```TypeScript
function end(scene: string): void
```

用于标记用户场景结束，用户场景结束时调用此接口。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scene | string | 是 |
