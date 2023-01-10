package com.kirin.test_json.bean;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * @author Xiyao Li
 * @date 2022/12/24 02:09
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class CounterInfo {
    private String name;
    private String src;
    private Double winRate;
    private Double games;
}
