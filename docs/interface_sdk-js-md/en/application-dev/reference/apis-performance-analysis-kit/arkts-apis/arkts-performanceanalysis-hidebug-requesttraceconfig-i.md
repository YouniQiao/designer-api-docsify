# RequestTraceConfig

�ṩtrace�ɼ��Ĳ���ѡ�

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

<!--Device-hidebug-interface RequestTraceConfig--><!--Device-hidebug-interface RequestTraceConfig-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## Modules to Import

```TypeScript
import { hidebug } from 'kits/@kit.PerformanceAnalysisKit';
```

## bufferSizeKb

```TypeScript
bufferSizeKb: int
```

trace�ļ��Ļ����С����KBΪ��λ����ֵΪ32λ�޷����������֣�������Ч��Χ��������ֵ�����ȡֵ��ΧΪ[1024, 15360]�������������ȡֵ��Χ��������������Ϊ����ı߽�ֵ��

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-RequestTraceConfig-bufferSizeKb: int--><!--Device-RequestTraceConfig-bufferSizeKb: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## durationMs

```TypeScript
durationMs: int
```

trace�ɼ�ʱ������msΪ��λ����ֵΪ32λ�޷����������֣�������Ч��Χ��������ֵ�����ȡֵ��ΧΪ[1000, 15000]�������������ȡֵ��Χ��������������Ϊ����ı߽�ֵ��

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-RequestTraceConfig-durationMs: int--><!--Device-RequestTraceConfig-durationMs: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## identifier

```TypeScript
identifier: string
```

�ɼ�trace������ļ���ǰ׺���ļ���ǰ׺ֻȡ�ַ���ǰ20���ַ����������ֽ�������ǰ20���ַ�ֻ������Сд��ĸ���»��ߣ�����������Ĭ��Ϊ���ַ�����

**Type:** string

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-RequestTraceConfig-identifier: string--><!--Device-RequestTraceConfig-identifier: string-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

## reserved

```TypeScript
reserved: int
```

Ԥ���ֶΣ���������Ϊ0��

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-RequestTraceConfig-reserved: int--><!--Device-RequestTraceConfig-reserved: int-End-->

**System capability:** SystemCapability.HiviewDFX.HiProfiler.HiDebug

