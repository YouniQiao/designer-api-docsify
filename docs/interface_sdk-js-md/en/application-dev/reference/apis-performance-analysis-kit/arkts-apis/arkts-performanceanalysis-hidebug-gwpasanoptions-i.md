# GwpAsanOptions

GWP-ASan����������������Ƿ�ʹ�ܡ�����Ƶ�ʣ��Լ�������Ĳ������

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-hidebug-interface GwpAsanOptions--><!--Device-hidebug-interface GwpAsanOptions-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## alwaysEnabled

```TypeScript
alwaysEnabled?: boolean
```

�����Ƿ�ÿ��������ʹ��GWP-ASan��true��100%ʹ��GWP-ASan��false��1/128����ʹ��GWP-ASan��Ĭ��ֵ��false��

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-GwpAsanOptions-alwaysEnabled?: boolean--><!--Device-GwpAsanOptions-alwaysEnabled?: boolean-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## isRecover

```TypeScript
isRecover?: boolean
```

���ڿ���Ӧ����100%���ʿ���GWP-ASanʱ���Ƿ��Կɻָ�ģʽ���С�true����GWP-ASan��100%���ʿ���ʱ��Ӧ���Կɻָ�ģʽ���С�false����GWP-ASan��100%���ʿ���ʱ��Ӧ���Բ��ɻָ�ģʽ���С�Ĭ��ֵ��false��ע�⣺�ò���ֻ��"��100%���ʿ���GWP-ASan"��������Ч��1/128���ʿ���������Ĭ��Ϊ�ɻָ�������isRecover���ơ�

**Type:** boolean

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GwpAsanOptions-isRecover?: boolean--><!--Device-GwpAsanOptions-isRecover?: boolean-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## maxSimutaneousAllocations

```TypeScript
maxSimutaneousAllocations?: int
```

������Ĳ������Ĭ��ֵΪ1000����Ҫ�������0����������������С��������ȡ����������þ�ʱ���·�����ڴ潫�����ܼ�ء��ͷ���ʹ�õ��ڴ����ռ�õĲ�۽��Զ����á�����ֵ��<=20000���������ܵ���VMA���ޱ�����

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-GwpAsanOptions-maxSimutaneousAllocations?: int--><!--Device-GwpAsanOptions-maxSimutaneousAllocations?: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## sampleRate

```TypeScript
sampleRate?: int
```

GWP-ASan����Ƶ�ʣ�Ĭ��ֵΪ2500����Ҫ�������0����������������С��������ȡ����1/sampleRate�ĸ��ʶԷ�����ڴ���в���������ֵ��>=1000����С������Ӱ�����ܡ�

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-GwpAsanOptions-sampleRate?: int--><!--Device-GwpAsanOptions-sampleRate?: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

