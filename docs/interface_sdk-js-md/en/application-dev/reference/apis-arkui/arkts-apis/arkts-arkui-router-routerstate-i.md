# RouterState

页面状态信息。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-router-interface RouterState--><!--Device-router-interface RouterState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { router } from 'kits/@kit.ArkUI';
```

## index

```TypeScript
index: number
```

表示当前页面在页面栈中的索引。从栈底到栈顶，index从1开始递增。

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RouterState-index: number--><!--Device-RouterState-index: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## name

```TypeScript
name: string
```

表示当前页面的名称，即对应文件名。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RouterState-name: string--><!--Device-RouterState-name: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## params

```TypeScript
params: Object
```

表示当前页面携带的参数。

**说明：** params参数只能传递可序列化的参数，不能传递方法和系统接口返回的对象（例如，媒体接口定义和返回的PixelMap对象）。建议开发者提取系统接口返回的对象中需要被传递的基础类型属性，自行构造object类型对象进行传递。

从API version 12开始，该接口支持在原子化服务中使用。

此接口仅可在Stage模型下使用。

**Type:** Object

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RouterState-params: Object--><!--Device-RouterState-params: Object-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## path

```TypeScript
path: string
```

表示当前页面的路径。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RouterState-path: string--><!--Device-RouterState-path: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

