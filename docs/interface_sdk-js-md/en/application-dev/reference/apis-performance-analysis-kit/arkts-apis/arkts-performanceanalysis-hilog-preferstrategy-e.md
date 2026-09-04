# PreferStrategy

Enumerates the preference strategies.

**Since:** 21

**System capability:** SystemCapability.HiviewDFX.HiLog

## UNSET_LOGLEVEL

```TypeScript
UNSET_LOGLEVEL = 0
```

The setting is cleared. The system-controlled minimum log level takes effect.

**Since:** 21

**Atomic service API:** This API can be used in atomic services since API version 21.

**System capability:** SystemCapability.HiviewDFX.HiLog

## PREFER_CLOSE_LOG

```TypeScript
PREFER_CLOSE_LOG = 1
```

The larger value of the new log level and the system-controlled minimum log level takes effect.

**Since:** 21

**Atomic service API:** This API can be used in atomic services since API version 21.

**System capability:** SystemCapability.HiviewDFX.HiLog

## PREFER_OPEN_LOG

```TypeScript
PREFER_OPEN_LOG = 2
```

The smaller value of the new log level and the system-controlled minimum log level takes effect.

**Since:** 21

**Atomic service API:** This API can be used in atomic services since API version 21.

**System capability:** SystemCapability.HiviewDFX.HiLog

**Examples**

The following example describes how to print five HiLog logs of different levels and call the setLogLevel API twice when the global log level is INFO:

```TypeScript
hilog.info(0x0001, "testTag", 'this is an info level log, id: %{public}d', 1);
hilog.setLogLevel(hilog.LogLevel.WARN, hilog.PreferStrategy.PREFER_OPEN_LOG);
hilog.info(0x0001, "testTag", 'this is an info level log, id: %{public}d', 2);
hilog.error(0x0001, 'testTag', 'this is an error level log, id: %{public}d', 3);
hilog.setLogLevel(hilog.LogLevel.DEBUG, hilog.PreferStrategy.PREFER_CLOSE_LOG);
hilog.debug(0x0001, "testTag", 'this is a debug level log, id: %{public}d', 4);
hilog.info(0x0001, "testTag", 'this is an info level log, id: %{public}d', 5);
```

The first log is printed properly because the global log level is INFO.
When the minimum log level of the process is set to WARN and the PREFER_OPEN_LOG is strategy selected, the actual minimum log level is INFO. Therefore, the second and third logs can be printed properly.
When the minimum log level of the process is set to DEBUG and the PREFER_CLOSE_LOG strategy is selected (equivalent to hilog.setMinLogLevel(hilog.LogLevel.DEBUG)), the fourth log cannot be printed because the global log level is INFO. The fifth log can be printed.
The log result is as follows:

```TypeScript
08-07 23:50:01.532   13694-13694   A00001/testTag                  com.example.hilogDemo  I     this is an info level log, id: 1
08-07 23:50:01.532   13694-13694   A00001/testTag                  com.example.hilogDemo  I     this is an info level log, id: 2
08-07 23:50:01.532   13694-13694   A00001/testTag                  com.example.hilogDemo  E     this is an error level log, id: 3
08-07 23:50:01.532   13694-13694   A00001/testTag                  com.example.hilogDemo  I     this is an info level log, id: 5
```
