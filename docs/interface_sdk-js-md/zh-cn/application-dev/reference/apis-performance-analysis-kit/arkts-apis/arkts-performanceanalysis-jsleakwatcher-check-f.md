# check

## 导入模块

```TypeScript
import { jsLeakWatcher } from 'kits/@kit.PerformanceAnalysisKit';
```

## check

```TypeScript
function check(): string
```

��ȡ��ͨ��jsLeakWatcher.watchע�ᷢ��й©�Ķ����б�������GC��δ�����յĶ���ᱻ���Ϊй©��

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为26.1.0。

<!--Device-jsLeakWatcher-function check(): string--><!--Device-jsLeakWatcher-function check(): string-End-->

**系统能力：** SystemCapability.HiviewDFX.HiChecker

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | ����GC��δ�����յ�й©�����б��� &lt;br&gt;**˵��**��check�ɹ�������JSON��ʽ��й©�����б���checkʧ�ܣ����ؿ��ַ����� |

## 示例

```TypeScript
let leakObjlist:string = jsLeakWatcher.check();
```

