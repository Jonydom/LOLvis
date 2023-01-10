package com.kirin.test_json.bean;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

/**
 * @author Xiyao Li
 * @date 2022/12/24 01:51
 */
@Data
@AllArgsConstructor
@NoArgsConstructor
public class RuneInfo {
    private List<String> rune;
    private Double pickRate;
    private Double games;
    private Double winRate;
}
