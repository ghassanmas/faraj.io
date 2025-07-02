import child_process from "node:child_process";
export default function() {
    //REF: https://github.com/saneef/eleventy-plugin-git-commit-date/blob/main/src/getGitCommitDateFromPath.js
    const latestGitCommitHash =
        child_process
            .execSync('git rev-parse --short HEAD')
            .toString()
            .trim();

    return {
        hash: latestGitCommitHash,
        buildTime: new Date()
    }
}